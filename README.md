# Football-Analysis
**INTRODUCTION**

The objective of this project is to detect and track players, referees, and footballs in video footage using YOLO, one of the most advanced AI object detection models. We will further train the model to improve its accuracy. To assign players to their respective teams, we will utilize K-means clustering for pixel segmentation based on the colors of their jerseys. This will enable us to calculate each team's ball possession percentage during a match. Additionally, we will employ optical flow to measure camera movements between frames, which allows for precise tracking of player movements. By implementing perspective transformation, we can account for depth and perspective in the scene, enabling us to measure player movements in meters rather than pixels. Finally, we will compute each player's speed and the distance they have covered. This comprehensive project addresses various concepts and real-world challenges, making it valuable for both novice and experienced machine learning engineers.

**Modules Utilized**

This project leverages several key modules to achieve its objectives:

- **YOLO (You Only Look Once)**: An advanced AI object detection model used for identifying and tracking players, referees, and footballs within video footage.
- **K-Means Clustering**: Employed for pixel segmentation and clustering to detect the colors of players' jerseys, which helps in assigning players to their respective teams based on t-shirt color.
- **Optical Flow**: Utilized to measure camera movement between frames, enabling accurate tracking of player movements even when the camera is in motion.
- **Perspective Transformation**: Applies geometric transformations to account for scene depth and perspective, allowing for the measurement of player movements in meters rather than pixels.
- **Speed and Distance Calculation**: Computes the speed and total distance covered by each player during the match.

**Trained Models**

- **Trained YOLO v5 Model**: A custom-trained version of the YOLO v5 model tailored specifically for this project to enhance detection accuracy for players, referees, and footballs.

**Sample Video**

- **Sample Input Video**: A provided video clip used to test and demonstrate the capabilities of the detection, tracking, and analysis systems implemented in the project.

**Requirements**

To run this project successfully, ensure you have the following installed:

- **Python 3.x**
- **Ultralytics**: For implementing the YOLO model.
- **Supervision**: For tracking and managing detection outputs.
- **OpenCV**: For computer vision tasks such as image processing and perspective transformation.
- **NumPy**: For numerical computations and array manipulations.
- **Matplotlib**: For plotting and visualizing data.
- **Pandas**: For data manipulation and analysis.
