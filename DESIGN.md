# PrepAI- System Design Document

## 1. Overview
PrepAI is designed to improve student learning outcomes through adaptive questioning and reinforcement techniques. This document outlines the system architecture, data flow, key components, and API endpoints.

## 2. System Architecture
### 2.1 Components
- **Frontend**: Mobile app for students to engage with the system.
- **Backend**: AI engine for question adaptation, user data processing, and performance tracking.
- **Database**: Stores student responses, question sets, analytics, and longitudinal statistical analysis data.
- **Notification System**: Pushes questions and reminders at strategic intervals.
- **Analytics Engine**: Runs statistical analysis to find correlations and trends in student mistakes.

### 2.2 Tech Stack
- **Frontend**: React Native (iOS & Android support)
- **Backend**: Python (FastAPI or Django for API endpoints)
- **Database**: PostgreSQL for structured data storage
- **AI Engine**: TensorFlow/PyTorch for question selection and response analysis
- **Analytics Engine**: Pandas/NumPy for statistical analysis of mistakes over time
- **Notification System**: Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNs)

## 3. Data Flow
1. **Student Interaction**
   - Takes an initial assessment
   - Answers multiple-choice questions (10 choices per question)
   - Data is logged into the system

2. **AI Processing**
   - Analyzes incorrect responses
   - Reorders answer choices to prevent pattern recognition
   - Identifies mistake patterns (e.g., misreading, misinterpretation)

3. **Statistical Analysis & Correlation Mapping**
   - Runs longitudinal analysis of student mistakes
   - Compares student errors against similar student profiles (e.g., handedness)
   - Finds correlations and patterns to inform new testing approaches 
   
4. **Reinforcement Delivery**
   - Sends targeted push notifications with previously missed questions
   - Engages students throughout the day for retention
   - Updates student performance records dynamically

## 4. Personalization Features
- Collects **handedness** (left/right) and **gender** (male/female) to analyze cognitive learning trends
- Generates customized question sets based on mistake history
- Adapts difficulty dynamically based on student progress
- Uses statistical modeling to compare student mistakes against similar profiles and recommend alternative testing approaches

## 5. API Endpoints & CRUD Methods
### 5.1 Authentication
- **Register a user** (`POST /api/register`)
  - Creates a new user with username, handedness, and gender.
  - **Request:**
    ```json
    {
      "username": "john_doe",
      "handedness": "right",
      "gender": "male"
    }
    ```
  - **Response:**
    ```json
    {"message": "User registered successfully"}
    ```

- **User login** (`POST /api/login`)
  - Authenticates user credentials.
  - Returns authentication token for session management.

### 5.2 Question Management
- **Retrieve all questions** (`GET /api/questions`)
  - Returns all available questions.

- **Retrieve a specific question** (`GET /api/questions/{question_id}`)
  - Fetches a single question by its ID.

- **Submit an answer** (`POST /api/questions/submit`)
  - Logs the student’s answer and updates performance tracking.
  - **Request:**
    ```json
    {
      "username": "john_doe",
      "question_id": 1,
      "selected_answer": 2
    }
    ```
  - **Response:**
    ```json
    {"correct": true}
    ```

- **Get missed questions** (`GET /api/questions/missed/{username}`)
  - Returns a list of missed questions for reinforcement.

### 5.3 Performance Tracking & Statistical Analysis
- **Fetch student progress** (`GET /api/performance/progress/{username}`)
  - Retrieves statistics on student performance.

- **Identify mistake categories** (`GET /api/performance/errors/{username}`)
  - Analyzes trends in incorrect responses.
  
- **Run statistical analysis on mistakes** (`GET /api/performance/analysis/{username}`)
  - Compares student errors with other similar profiles to find learning patterns and new testing methods.
  
### 5.4 Admin Management
- **Add a new question** (`POST /api/questions/add`)
  - **Request:**
    ```json
    {
      "question": "What is 5 + 3?",
      "answers": ["6", "7", "8", "9", "10"],
      "correct": 2
    }
    ```

- **Update a question** (`PUT /api/questions/{question_id}`)
  - Allows modification of existing questions.

- **Delete a question** (`DELETE /api/questions/{question_id}`)
  - Removes a question from the system.

## 6. Notification & Engagement
- Push notifications triggered based on missed questions.
- Adjustable frequency settings to balance engagement and avoidance.
- Gamification elements (streaks, achievements) to encourage participation.

## 7. Future Enhancements
- Expand AI model for personalized learning styles.
- Integrate voice-based AI for verbal question practice.
- Develop API for integration with school LMS platforms.

## 8. Security & Compliance
- **Data Encryption**: All user data is encrypted at rest and in transit.
- **Privacy Compliance**: GDPR and COPPA compliant for student data protection.
- **Access Control**: Role-based authentication for students and educators.

## 9. Deployment & Scaling Strategy
- Deployed on AWS/GCP with auto-scaling groups.
- Containerized using Docker & Kubernetes.
- CI/CD pipeline for continuous updates and improvements.

## 10. Conclusion
The AI Prep Tool is built to provide a robust, adaptive learning experience by continuously analyzing student performance and reinforcing concepts. By leveraging AI-driven error detection, customized notifications, and statistical analysis of learning patterns, the system evolves testing strategies dynamically to improve student mastery.
