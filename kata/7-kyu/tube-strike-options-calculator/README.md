# Tube Strike Options Calculator

**Kata Link:** [https://www.codewars.com/kata/568ade64cfd7a55d9300003e/python](https://www.codewars.com/kata/568ade64cfd7a55d9300003e/python)

## The Sweaty Bus Ride

There is a tube strike today so instead of getting the London Underground home you have decided to take the bus. It's a hot day and you have been sitting on the bus for over an hour, but the bus is hardly moving. Your arm is sticking to the window and sweat drips off your nose as you try to read your neighbour's book when you say to yourself, "This is ridiculous. I could have walked faster than this!" 

Suddenly you have an idea for an app that helps people decide whether to walk or take the bus home when the London Underground is on strike. You rush home (relatively speaking) and begin to define the function that will underpin your app.

## Function Specification

You must create a function which takes three parameters:
- **walking distance home**: distance to walk directly home (in kilometres)
- **distance the bus must travel**: distance the bus travels (in kilometres)  
- **combined walking distance**: total distance of walking from office to bus stop and from bus stop to house (in kilometres)

### Example Scenario

If your home is 5km away by foot, and the bus that takes you home travels 6km, but you have to walk 500 metres to the bus stop to catch it and 500 metres to your house once the bus arrives (i.e. 1km in total), which is faster, walking or taking the bus?

### Which of these is faster?

```
Option 1: Start ---Walk 5km---> End
Option 2: Start ---Walk 500m---Bus 6km---Walk 500m---> End
```

### Speed Variables

Walking speed and bus driving speed have been given to you as two pre-loaded variables (`$global_variables` in Ruby):

- `walk = 5` (km/hr)
- `bus = 8` (km/hr)

### Return Requirements

The function must return the fastest option, either `"Walk"` or `"Bus"`. 

**Special cases:**
- If the walk is going to be **over 2 hours**, the function should recommend that you take the bus
- If the walk is going to be **under 10 minutes**, the function should recommend that you walk
- If both options are going to take the **same amount of time**, the function should recommend that you walk

## Tags

`#Fundamentals` `#Algorithms`