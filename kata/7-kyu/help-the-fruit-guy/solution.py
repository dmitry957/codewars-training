def remove_rotten(bag_of_fruits):
  return ([fruit.replace('rotten', '').lower() for fruit in bag_of_fruits]
          if bag_of_fruits
          else [])