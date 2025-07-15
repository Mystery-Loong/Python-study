alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_position':0,'y_position':25,'speed':'fast'}
# print(f"Original position: {alien_0['x_position']}")

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
# if alien_0['speed'] == 'slow':
#     x_incerment = 1
# elif alien_0['speed'] == 'medium':
#     x_incerment = 2
# else:
    # 这个外星人的移动速度为快
    # x_incerment = 3

# 新位置为旧位置加上移动距离
# alien_0['x_position'] = alien_0['x_position'] + x_incerment

# print(f"New position: {alien_0['x_position']}")

print(alien_0)

del alien_0['points']
print(alien_0)