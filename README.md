# Fast attendance #
This is an application to increase the speed of marking attendance in distinct events in the Innopolis University,
such as club meetings or tests/exams of courses.

---

## How to work with ##
To use this application, enter this [website]().
If you did not register before, do it [here]() using your innopolis email (for example, g.bush@innopolis.university).
To get the file with all emails, you have to upload the photo in the [upload page]().

To run your own application, clone this repo and run the command in the console `streamlit run application.py`.
Remember that you have to install the necessary libraries for the project.

(how to store the data)

---

## Dependencies ##
All required packages you may find in the [requirements.txt]() file.
You also can copy these commands and run them on your machine:
```shell
pip install torch torchvision -f https://download.pytorch.org/whl/cu11X # change X to the number of the cuda version on your machine
pip install matplotlib numpy tqdm uuid opencv facenet-pytorch streamlit
```

---

## References ##

To develop the project, we used distinct sources:
- [OpenCV Cascade classifier](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html) to detect faces in the photo
- [MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf) taken from the [facenet-pytorch](https://github.com/timesler/facenet-pytorch) library

---

## Authors ##
The project was made by 3 students of Innopolis University:
[Smulemun](https://github.com/Smulemun), [xFonzie](https://github.com/xFonzie) and [Zener085](https://github.com/Zener085)