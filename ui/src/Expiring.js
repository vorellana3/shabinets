import {Component} from "react";

class Expiring extends Component {
  constructor(props) {
    super(props);

    this.state = {nextExpiring: []};
    
    this.updateExpiring = this.updateExpiring.bind(this);
    this.getExpiring = this.getExpiring.bind(this);
    this.updateExpiring();
  }

  render(){
    return(
      <div className="expiring-list">
        {this.getExpiring()}
      </div>
    );
  }
  
  updateExpiring() {
    fetch('http://localhost:5000/expired-foods')
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
        <div className="expiring-item">
          <div className="expiring-item-name">{(i+1) + ". " + this.state.nextExpiring[i][0]}</div>
          <div className="expiring-item-date">{this.state.nextExpiring[i][1]}</div>
        </div>
      );
    }
    return comps;
  }
  
  
}

export default Expiring;
