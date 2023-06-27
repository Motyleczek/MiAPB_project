import requests
import csv

# REST API endpoint URL
api_url = "http://localhost:8080/engine-rest/engine/default/history/activity-instance"

# Prompt the user to enter the Process Instance ID
process_instance_id = input("Enter the Process Instance ID: ")

# Send GET request to the API endpoint with the process instance ID as a query parameter
response = requests.get(api_url, params={"processInstanceId": process_instance_id})

# Check if the request was successful
if response.status_code == 200:
    # Extract JSON data from the response
    json_data = response.json()

    # Extract relevant information from JSON data
    data = []
    for item in json_data:
        data.append({
            'Activity ID': item['activityId'],
            'Activity Name': item['activityName'],
            'Activity Type': item['activityType'],
            'Assignee': item['assignee'],
            'Called Process Instance ID': item['calledProcessInstanceId'],
            'Called Case Instance ID': item['calledCaseInstanceId'],
            'Canceled': item['canceled'],
            'Complete Scope': item['completeScope'],
            'Duration In Millis': item['durationInMillis'],
            'End Time': item['endTime'],
            'Execution ID': item['executionId'],
            'ID': item['id'],
            'Parent Activity Instance ID': item['parentActivityInstanceId'],
            'Process Definition ID': item['processDefinitionId'],
            'Process Instance ID': item['processInstanceId'],
            'Start Time': item['startTime'],
            'Task ID': item['taskId'],
            'Tenant ID': item['tenantId'],
            'Removal Time': item['removalTime'],
            'Root Process Instance ID': item['rootProcessInstanceId'],
        })

    # Save the data to a CSV file with a specified delimiter
    csv_filename = input("Give csv file name: ")
    csv_filename = "logs_folder/" + csv_filename + ".csv"
    delimiter = ';'  # Specify the desired delimiter here
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)

    print(f"Activity instance logs saved to {csv_filename}")
else:
    print(f"Error accessing the API: {response.status_code} - {response.text}")
