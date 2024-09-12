# Centralized Microservice Logging System

## Problem Overview

In a microservices architecture, each service generates logs that are centralized for easy analysis. The goal of this project is to:
- Consolidate the most **recent log entries** from various services.
- **Sort** these log entries by date and time in descending order (newest first).

## Input

A list of dictionaries where each dictionary represents a batch of logs from different microservices, each containing:
- **service_name**: Name of the microservice.
- **log_type**: Log severity (INFO, ERROR, DEBUG, WARN).
- **date**: Date of log generation.
- **time**: Time of log generation.

### Example Input:
```json
[
  {
    "micro-service-a1": {'log_type': 'INFO', 'date': 'Wed July 24 2023', 'time': '12:30:00 GMT+0530'},
    "micro-service-b2": {'log_type': 'DEBUG', 'date': 'Wed July 24 2023', 'time': '12:50:00 GMT+0530'}
  }
]
```

## Output

A list of consolidated logs:
- **Most recent logs** from each service.
- Sorted by date and time (newest to oldest).

### Example Output:
```json
[
  {"date": "2023-07-24", "time": "12:50:00 GMT+0530", "service_name": "micro-service-b2", "log_type": "DEBUG"},
  {"date": "2023-07-24", "time": "12:30:00 GMT+0530", "service_name": "micro-service-a1", "log_type": "INFO"}
]
```

## Solution

This project:
- Collects the most recent log entries for each service.
- Formats the date and time to ensure correct sorting.
- Sorts the logs in descending order.

## How to Run

1. Clone the repository.
2. Run the `sorted_logs` function with your log entries.
   NOTE : Example testcase is given for reference. 