## Problem Description From My Understanding
We need to create a system that efficiently handles asynchronous tasks for multiple customers sharing the same server resources. The system needs to:
- Handle different types of jobs based on execution time
- Manage customers based on their data volume
- Distribute tasks efficiently across workers
- Track and monitor task execution

## Implementation Guide

## Core Components

### 1. Customer Classification (Volume-Based)
* LOW: 1-3 sites
* MEDIUM: 4-10 sites
* HIGH: >10 sites
* Rationale: Customers with more sites will generate more tasks and consume more resources

### 2. Job Classification (Time-Based)
* VERY_FAST: > 480s
* FAST: ≤ 480s
* MEDIUM: ≤ 360s
* SLOW: ≤ 240s
* VERY_SLOW: < 120s
* Rationale: Different execution times require different resource allocation strategies

### 3. Queue Management
* Each combination of customer volume and job speed gets a dedicated queue
* Example queues:
   * HIGH_VOLUME_VERY_SLOW: For high-volume customers running time-intensive tasks
   * LOW_VOLUME_FAST: For low-volume customers running quick tasks
* Total Queues: 15 (3 customer types × 5 job speeds)
* Rationale: Segregation prevents resource hogging by heavy tasks

### 4. Worker Distribution
* Workers are assigned to specific queues
* Each worker handles one task at a time
* Workers can be scaled independently based on queue load
* Rationale: Dedicated workers ensure fair resource distribution


## Technical Architecture

### Data Storage
1. Redis
   * Used as message broker
   * Stores task queues and results
   * Fast in-memory operations

2. Database Tables
   * Site: Stores customer site information
   * UserRecords: Stores user data for each site
   * Job: Stores job definitions and execution times
   * UserJobStatus: Tracks job execution status
   * UserJobsDetails: Links users, jobs, and sites


### Task Processing Flow
1. Task Submission
   * Client submits task via API
   * System determines customer volume and job type
   * Task is routed to appropriate queue

2. Task Execution
   * Worker picks up task from assigned queue
   * Updates status (PENDING → IN_PROGRESS)
   * Executes task
   * Updates final status (COMPLETED/FAILED)

3. Status Tracking
   * Each task gets unique UUID
   * Status updates stored in database
   * Clients can poll status via API

## Monitoring and Scaling

### Metrics to Monitor
* Task execution times
* Worker utilization
* Error rates
* Customer volume changes

### Scaling Strategies
1. Horizontal Scaling
   * Add more workers for busy queues
   * Remove workers from idle queues

2. Queue Rebalancing
   * Redistribute tasks if queues become unbalanced
   * Adjust worker assignments based on load
