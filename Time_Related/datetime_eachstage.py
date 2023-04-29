from datetime import datetime
# Calculate the duration of each stage based on the recorded time stamps of 
# reaching each altitude.


# Copy all timestamp records from the txt file
t1 = '2023-03-21 09:46:20.666'      # 1500 / 1.27
t2 = '2023-03-21 09:49:29.610'      # 2000 / 1.78
t3 = '2023-03-21 09:58:02.192'      # 2500 / 2.38
t4 = '2023-03-21 10:07:19.695'      # 3000 / 2.95
t5 = '2023-03-21 10:16:55.639'      # 3500 / 3.5
t6 = '2023-03-21 10:27:52.062'      # 4000 / 4.1

t1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S.%f')  # Text parsing
t1x = datetime.timestamp(t1)                        # Std time to timestamp
t2 = datetime.strptime(t2, '%Y-%m-%d %H:%M:%S.%f')
t2x = datetime.timestamp(t2)
t3 = datetime.strptime(t3, '%Y-%m-%d %H:%M:%S.%f')
t3x = datetime.timestamp(t3)
t4 = datetime.strptime(t4, '%Y-%m-%d %H:%M:%S.%f')
t4x = datetime.timestamp(t4)
t5 = datetime.strptime(t5, '%Y-%m-%d %H:%M:%S.%f')
t5x = datetime.timestamp(t5)
t6 = datetime.strptime(t6, '%Y-%m-%d %H:%M:%S.%f')
t6x = datetime.timestamp(t6)

print('1.5k-2k Time:', round((t2x-t1x)/60), 'min', round((t2x-t1x)%60), 's')
print('2k-2.5k Time:', round((t3x-t2x)/60), 'min', round((t3x-t2x)%60), 's')
print('2.5k-3k Time:', round((t4x-t3x)/60), 'min', round((t4x-t3x)%60), 's')
print('3k-3.5k Time:', round((t5x-t4x)/60), 'min', round((t5x-t4x)%60), 's')
print('3.5k-4k Time:', round((t6x-t5x)/60), 'min', round((t6x-t5x)%60), 's')

# Total time taken from 1.5k to 4k altitude
# 5 min experiment time after reaching 4k
# The total experiment time is:
print('Whole Time:', round((t6x-t1x)//60)+5, 'min', round((t6x-t1x)%60), 's+')
