//var Devices = require('./components/device/device.js');
import Devices from './components/device/device';
function devices() {
  $.ajax({
    url: '/api/manage/device-activity',
    success: (data) => {
      data = JSON.parse(data);
       ReactDOM.render(
       <Devices deviceList={data}/>
         , document.getElementById('devices'));
    },
    type: 'GET'
  });
}

module.exports = devices;
