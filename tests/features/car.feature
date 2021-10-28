# Created by jmill at 10/28/2021
Feature: Accelerator on Car
  As a driver of a car
  I want to be able to accelerate, break and know how fast I am driving
  So I don't get in an accident

  Scenario: Acceleration
    Given the car speed is "20" miles per hour
    When I accelerate
    Then the speed is "25" miles per hour

  Scenario: Brake
    Given the car speed is "30" miles per hour
    When I brake
    Then the speed is "25" miles per hour