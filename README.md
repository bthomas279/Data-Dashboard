# Data-Dashboard

## 📝 Introduction

The goal of this project was to create a Dash App that visualizes data from the Student Habits vs Acedemic Performance database. Through these dash visualizations, I hope to uncover some trends of the kinds of factors that effect acedemic performance, and then determine the results this database shows.

---

## ✅ Features

- Extracts various data information from the CSV into the visualizations needed
- Updates app from any script as long as the app_main is active.

---

## 📁 Project Structure

Data Dashboard
│
├── exam_scores.py ← Exam score visualization
├── media_vs_sleep.py ← Social media hours vs sleep hours visualization
├── study_vs_media.py ← Study hours vs social media hours by gender visualization
├── diet_vs_mental.py ← Diet Quality vs mental health rating visualization
├── sleep_vs_exam.py ← Sleep hours vs exam score visualization
├── sleep_vs_mental.py ← Sleep hours vs mental health rating by part time job visualization
├── mental_vs_exam.py ← Mental health rating vs exam score visualization
└── database.csv ← Database used for this project

api
└── app_main.py ← Main Dash app

## 🔧 Core Modules

- **[diet_vs_mental.py](https://github.com/bthomas279/Data-Dashboard/blob/main/diet_vs_mental.py)**

Creates violin plot for diet quality and mental health rating.

- **[exam_scores.py](https://github.com/bthomas279/Data-Dashboard/blob/main/exam_scores.py)**

Creates histogram of exam scores.

- **[media_vs_sleep.py](https://github.com/bthomas279/Data-Dashboard/blob/main/media_vs_sleep.py)**

Creates boxplot of social media hours and sleep hours

- **[mental_vs_exam.py](https://github.com/bthomas279/Data-Dashboard/blob/main/mental_vs_exam.py)**

Creates density heatmap of mental health scores and exam scores

- **[sleep_vs_exam.py](https://github.com/bthomas279/Data-Dashboard/blob/main/sleep_vs_exam.py)**

Creates contour Plot of sleep hours and exam scores

- **[sleep_vs_mental.py](https://github.com/bthomas279/Data-Dashboard/blob/main/sleep_vs_mental.py)**

Creates line plot of sleep hours and mental health rating

- **[study_vs_media.py](https://github.com/bthomas279/Data-Dashboard/blob/main/study_vs_media.py)**

Creates grouped Bar chart of study hours and social media hours.

---

## 🚀 How to Use

Simpily run the visualization scripts first and then run app_main to activate the app. Use this link (http://127.0.0.1:8050/) to view the app. Edits and additions can be made to the the visualization scripts. Simpily make these changes in the chosen visualization script(s) and run them. This will update the app as long as the app_main is running.

---

## 🔮 Future Plans

I do not have any future plans for this project at the moment. However, this was a very engaging and interesting project to complete, and I will use the skills and modules I learned here for potential future projects.

---

## 👨‍💻 Creator Information

This project was developed by **Benjamin Thomas**

## References

The database used in this project is from the Student Habits vs Acedemic Performance database created by Jayanta Nath on Kaggle. This database (as of June 2025) is free to use. If you would like to use this database for yourself or check out the creator, use the Kaggle link below.
https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance/data
