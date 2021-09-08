#https://amazon-connect-introduction.workshop.aws/5.lab3.html

#Lambda Lookup 

import json
import boto3
import os
from boto3.dynamodb.conditions import Key

tableName= "UserInfo"
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
  print(event)
   #Customer phone number passed from Amazon Connect via JSON
  phoneNumber = event ['Details']['ContactData']['CustomerEndpoint']['Address']
  print(phoneNumber)

  #customer lookup to DynamoDB via Customer phone number
  table = dynamodb.Table("UserInfo")
  response = table.get_item(Key={'phoneNumber' : phoneNumber})
  print(response)

  #If record exists write values to variables
  if 'Item' in response:
    userId = response['Item']['userID']
    firstName = response['Item']['firstName']
    lastName = response['Item']['lastName']
    email = response['Item']['email']
    password = response['Item']['password']
    position = response['Item']['position']
    DOB = response['Item']['DOB']
    phoneNumber = response['Item']['phoneNumber']

    #Return variables to Amazon Connect
    return {'message': 'Success',
            'userId' : userId,
            'firstName' : firstName,
            'lastName' : lastName,
            'email' : email,
            'password' : password,
            'position' : position,
            'DOB' : DOB,
            'phoneNumber' : phoneNumber,
    }

    #If no match return a default message
  else:
      # print("Fail")
      return { 'message': 'Fail'}  
      

