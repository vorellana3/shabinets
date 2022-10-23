import {Component} from "react";

class Expiring extends Component {
  constructor(props) {
    super(props);

    this.state = {nextExpiring: [
      ["one", "12-12-2221"],
      ["two", "2-24-2000"],
      ["three", "10-24-2022"]
    ]};
    
    this.updateExpiring = this.updateExpiring.bind(this);
    this.getExpiring = this.getExpiring.bind(this);
    this.expiryHighlight= this.expiryHighlight.bind(this);
    //this.updateExpiring();
  }

  render(){
    return(
      <div className="expiring-list">
        <div className="expiring-list-header">Upcoming Expirations</div>
        {this.getExpiring()}
      </div>
    );
  }
  
  updateExpiring() {
    fetch('http://localhost:5000/api/expired-foods')
      .then(response => response.json())
      .then(response => {
          let arr = [];
        for (let item in response) {
          arr.push([item, response[item]]);
        }
          this.setState({nextExpiring: arr});
      });
  }

  getExpiring() {
    let comps = [];
    for (let i = 0; i < this.state.nextExpiring.length; i++) {
      comps.push(
        <div className={"expiring-item " + this.expiryHighlight(this.state.nextExpiring[i][1])}>
          <div className="expiring-item-name">{(i+1) + ". " + this.state.nextExpiring[i][0]}</div>
          <div className={"expiring-item-date"}>{this.state.nextExpiring[i][1]}</div>
        </div>
      );
    }
    return comps;
  }

  expiryHighlight(date) {
    let today = new Date();
    let split = date.split("-");
    let expiration = new Date(split[2], split[0]-1, split[1]);
    let remDays = (expiration - today) / (1000 * 3600 * 24);
    if (remDays < 0) {
      return "red";
    } else if (remDays < 2) {
      return "yellow";
    }
    return "";
  }
  
  
}

export default Expiring;
