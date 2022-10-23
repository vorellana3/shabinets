import {Component} from "react";

class Expiring extends Component {
  constructor(props) {
    super(props);

    this.nextExpiring = [
      ["first", "12-12-2022"],
      ["second", "9-18-2022"],
    ];
    
    this.updateExpiring = this.updateExpiring.bind(this);
    this.getExpiring = this.getExpiring.bind(this);
  }

  render(){
    return(
      <div className="expiring-list">
        {this.getExpiring()}
      </div>
    );
  }
  
  updateExpiring() {
    fetch(this.props.backend + '/expired-foods')
      .then(response => response.json())
      .then(response => {
        this.nextExpiring = "";
        for (let item in response) {
          this.nextExpiring.push([item, response[item]]);
        }
      });
  }

  getExpiring() {
    let comps = [];
    for (let i = 0; i < this.nextExpiring.length; i++) {
      comps.push(
        <div className="expiring-item">
          <div className="expiring-item-name">{i + ". " + this.nextExpiring[i][0]}</div>
          <div className="expiring-item-date">{this.nextExpiring[i][1]}</div>
        </div>
      );
    }
    return comps;
  }
  
  
}

export default Expiring;
