flowchart TD
    A[Input: User Preferences] --> B[Process: Load Songs CSV];
    B --> C[Initialize Empty Scores List];
    C --> D{Loop: For each song in CSV};
    D --> E[Calculate Score using Scoring Logic];
    E --> F[Store Score in List];
    F --> D;
    D --> G[Sort Scores in Descending Order];
    G --> H[Select Top K Songs];
    H --> I[Output: Top K Recommendations];