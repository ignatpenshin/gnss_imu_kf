from plot import Dead_reckoning

path = 'data/'
gnss_data = path + "gnss_2022-07-25T11-26-49.032515.txt"
imu_data = path + "lidar_1658737644300159744_IMU.log.csv"

if __name__ == "__main__":
    Dead_reckoning(gnss_data, imu_data)
    
