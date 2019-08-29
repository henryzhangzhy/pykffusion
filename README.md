# Python implementation of the multi sensor fusion using the Kalman Filter

## Release
- version 0.1.1 (branched off from master)
  - single sensor single object tracking
  - correct motion model
  - cleaner main loop
  - configurable figure display
- version 0.1
  - a center radar
  - plot the error in localization
  - plot the innovation


## TODO

- [ ] add lidar model
  - [x] generating lidar data
  - [ ] proposal generation based on lidar
- [ ] add box model
- [ ] add camera model
- [ ] collision detection
- [ ] occlusion
- [ ] adding delayed data
- [ ] adding asquent data
- [x] add moving to ego vehilcle
- [x] add text display
- [x] add radar model
- [x] add virtual sensor (use radar center mode instead)
- [x] add visualization to kalman filter
- [x] add log to kalman filter
- [x] correct point model
- [x] added forget time
- [x] allow turn on or off one view. (By set fig_name to None)
- [x] add more radar to test multi sensor
  - [x] fix merging similar track
  - [x] sensor order matters, figure out why? (updated in blog[1])
- [x] add kalman filter
- [x] add data association
- [x] multi object generation
  - [x] add speed limit
  - [x] add collision detection for generating object


Reference

[1] <https://zhyhenryzhang.github.io/2019/08/21/experimental-approach-to-understand-the-kalman-filter.html><br/>
[2] <https://zhyhenryzhang.github.io/2019/08/12/a-multi-sensor-fusion-system-for-moving-object-detection-and-tracking-in-urban-driving-environments.html><br/>
[3] <https://zhyhenryzhang.github.io/2019/08/18/multi-sensor-data-fusion-hugh-durrant-Whyte.html><br/>