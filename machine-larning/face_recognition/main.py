from time import time
import os, sys, cv2

import matplotlib.pyplot as plt
import numpy

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC


def cascade_detect(cascade, image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.astype(numpy.float32, copy=False)
    real_gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return real_gray_image, cascade.detectMultiScale(
        gray_image,
        scaleFactor = 1.15,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

def detections_draw(image, detections):
    crop_images = []
    for (x, y, w, h) in detections:
        # p = int(w/3)
        # cv2.rectangle(image, (x-p, y-p), (x + w+p, y + h+p), (0, 255, 0), 2)
        yc = y+h//2
        hm = int((h+h*.25)/2)
        xc = x+w//2
        wm = int(hm*.74)
        print("({0}, {1}, {2}, {3})".format(xc-wm, yc-hm, wm*2, hm*2))
        cv2.rectangle(image, (xc-wm, yc-hm), (xc+wm, yc + hm), (0, 255, 0), 2)
        crop_images.append(image[yc-hm:yc + hm, xc-wm:xc+wm])
    return crop_images

def plot_image(image, title=""):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8, 2.4))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    plt.subplot(1, 1, 1)
    plt.imshow(image, cmap=plt.cm.gray)
    if title:
        plt.title(title, size=12)
    plt.xticks(())
    plt.yticks(())

def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

def main(argv = None):
    if argv is None:
        argv = sys.argv

    # cascade_path = sys.argv[1]
    # image_path = sys.argv[2]
    cascade_path = "/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    # image_path = "/home/gbriones/Downloads/test2.jpg"
    image_path = "/home/gbriones/Downloads/tony_blair_00.jpg"
    result_path = sys.argv[3] if len(sys.argv) > 3 else None

    cascade = cv2.CascadeClassifier(cascade_path)
    # import pdb; pdb.set_trace()
    image = cv2.imread(image_path)
    if image is None:
        print("ERROR: Image did not load.")
        return 2

    gray_image, detections = cascade_detect(cascade, image)
    crop_images = detections_draw(gray_image, detections)
    resized_image = cv2.resize(crop_images[0], (37, 50))

    ###############################################################################
    # Download the data, if not already on disk and load it as numpy arrays

    lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

    # introspect the images arrays to find the shapes (for plotting)
    n_samples, h, w = lfw_people.images.shape

    # for machine learning we use the 2 data directly (as relative pixel
    # positions info is ignored by this model)
    X = lfw_people.data
    n_features = X.shape[1]

    # the label to predict is the id of the person
    y = lfw_people.target
    target_names = lfw_people.target_names
    n_classes = target_names.shape[0]
    n_components = 150
    print(target_names)

    # import pdb; pdb.set_trace()

    print("Extracting the top %d eigenfaces from %d faces"
          % (n_components, X.shape[0]))
    t0 = time()
    pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X)
    print("done in %0.3fs" % (time() - t0))

    eigenfaces = pca.components_.reshape((n_components, h, w))
    import pdb; pdb.set_trace()
    print("Projecting the input data on the eigenfaces orthonormal basis")
    t0 = time()
    X_pca = pca.transform(X)
    X_test_pca = pca.transform([resized_image.flatten()])
    print("done in %0.3fs" % (time() - t0))


    ###############################################################################
    # Train a SVM classification model

    print("Fitting the classifier to the training set")
    t0 = time()
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }

    if os.path.isfile('filename.pkl'):
        clf = joblib.load('filename.pkl')
    else:
        clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced', probability=True), param_grid)
        clf = clf.fit(X_pca, y)
        joblib.dump(clf, 'filename.pkl')
    print("done in %0.3fs" % (time() - t0))
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)

    print("Predicting people's names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("done in %0.3fs" % (time() - t0))
    print(y_pred[0])
    print(target_names[y_pred[0]])


    print("Found {0} objects!".format(len(detections)))
    if result_path is None:
        # cv2.imshow("Objects found", resized_image)
        # cv2.waitKey(0)
        # plot_image(resized_image)
        images = [resized_image.flatten()]
        # import pdb; pdb.set_trace()
        titles = ["Original"]
        for index in range(len(y)):
            if y[index] == y_pred[0] and len(images) < 12:
                images.append(X[index])
                titles.append(target_names[y[index]])
        plot_gallery(images, titles, h, w)
        eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
        plot_gallery(eigenfaces, eigenface_titles, h, w)
        plt.show()
    else:
        cv2.imwrite(result_path, image)

if __name__ == "__main__":
    sys.exit(main())
