class Devices extends React.Component {
  constructor(props) {
    super(props);
    this.state = {deviceList:props.deviceList};
  }
  componentDidMount() {
    this.checkInterval = setInterval(()=>{
      this.updateDeviceActivity();
    },5000);
    };
  componentWillUnmount() {
    console.log('component unmount');
    clearInterval(this.checkInterval);
    };
  updateDeviceActivity(){
    $.ajax({
    url: '/api/manage/device-activity',
    success: (data) => {
      data = JSON.parse(data);
      this.setState({
        deviceList:data
      });
    },
    type: 'GET'
  });
  }

  render() {
    let isWOL = function (WOL) {
      if(WOL)
        return (<div className="device--WOL"><button href="#" className="device__WOL">wake</button></div>);
      else
        return null;
    };
    let list = this.state.deviceList.map((device)=>
          <div className="device--item" key={device.id}>
            <div className="device--name">{device.name}</div>
            <div className="div">{device.WOL}</div>
            {isWOL(device.WOL)}
            <span className={'device--state device--state__'+device.state}>{device.state}</span>
            <hr/>
          </div>

        );

    return (
      <div className="device">
        {list}
      </div>
    )
  }
}

export default Devices
