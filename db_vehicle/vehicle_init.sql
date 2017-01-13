DROP DATABASE vehicle;
# to create database and tables
# create database vehicle character set utf8;
create database vehicle default charset utf8;
use vehicle;

create table vehicle_info(
id int(12) NOT NULL AUTO_INCREMENT,
id_device int(12) NOT NULL UNIQUE,
vin varchar(24) NOT NULL UNIQUE, 
type_vehicle varchar(24), 
fellow varchar(24) DEFAULT 'NO_ONE', 
licence_plate varchar(20) UNIQUE, 
miles_orignal int(7) DEFAULT 0,
miles_current int(7) DEFAULT 0, 
PRIMARY KEY (id)
);

create table vehicle_status(
id int(12) NOT NULL AUTO_INCREMENT, 
id_device int(12) NOT NULL, 
datetime_ DATETIME NOT NULL,
speed int(4) DEFAULT 0,
engine_rpm int(6) DEFAULT 0,
engine_load_cal int(3) DEFAULT 0,
engine_load_abs int(5) DEFAULT 0,
trim_long  varchar(40),
trim_short varchar(40),
timing_advance int(3) DEFAULT 0,
tmp_engine
int(3) DEFAULT 0,
tmp_water int(3) DEFAULT 0,
tmp_air_intake int(3) DEFAULT 0,
tmp_catalyst_B1S1 int(3) DEFAULT 0,
tmp_catalyst_B1S2 int(3) DEFAULT 0,
oxygen_sensor varchar(40),
air_flow_rate_MAF int(3) DEFAULT 0,
pos_throttle int(3) DEFAULT 0,
time_since_enginee   int(6) DEFAULT 0,
time_since_cleared  int(6) DEFAULT 0,
time_with_MIL int(6) DEFAULT 0,
pressure_barometric_abs int(3) DEFAULT 0,
cmd_evaporative_purge int(3) DEFAULT 0,
cmd_fuel_air_equ_ratio int(6) DEFAULT 0,
cmd_throttle_actuator int(3) DEFAULT 0,
warm_ups_since_cleared int(6) DEFAULT 0,
miles_since_cleared int(6) DEFAULT 0,
miles_with_MIL int(6) DEFAULT 0,
voltage int(2) DEFAULT 24,
fule_status int NOT NULL DEFAULT 0,
PRIMARY KEY (id),
FOREIGN KEY (id_device) REFERENCES vehicle_info(id_device)
);

create table vehicle_history(
id int(12) NOT NULL AUTO_INCREMENT, 
id_device int(12) NOT NULL, 
datetime_start DATETIME NOT NULL, datetime_stop DATETIME NOT NULL,
speed_avg int(4) DEFAULT 0, speed_min int(4) DEFAULT 0, speed_max int(4) DEFAULT 0,
engine_rpm_avg int(6) DEFAULT 0, engine_rpm_min int(6) DEFAULT 0, engine_rpm_max int(6) DEFAULT 0,
engine_load_avg int(3) DEFAULT 0, engine_load_min int(3) DEFAULT 0, engine_load_max int(3) DEFAULT 0,
tmp_engine_avg int(3) DEFAULT 0, tmp_engine_min int(3) DEFAULT 0, tmp_engine_max int(3) DEFAULT 0,
tmp_water_avg int(3) DEFAULT 0, tmp_water_min int(3) DEFAULT 0, tmp_water_max int(3) DEFAULT 0,
PRIMARY KEY (id),
FOREIGN KEY (id_device) REFERENCES vehicle_info(id_device)
);

# insert some vehicle_info
INSERT INTO vehicle_info(id_device, vin, licence_plate, miles_orignal, miles_current)
	VALUE(001001, 'LGBG2NE0XBY002169', '粤AH316U',0, 100);
INSERT INTO vehicle_info(id_device, vin, licence_plate, miles_orignal, miles_current)
	VALUE(001002, 'LGBG2NE0XBY002100', '粤AL220k',0, 256);

# insert some vehicle_status
INSERT INTO vehicle_status(id_device, datetime_, speed, engine_rpm, engine_load_cal, tmp_engine
, tmp_water)
	VALUE(001001, '2016-07-11 13:23:44', 50, 3000, 70, 200, 78);
INSERT INTO vehicle_status(id_device, datetime_, speed, engine_rpm, engine_load_cal, tmp_engine
, tmp_water)
	VALUE(001001, '2016-07-11 13:25:44', 80, 4000, 81, 300, 88);
