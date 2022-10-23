import {Component} from "react";

const backend = 'localhost:5000';

class PerishableField extends Component {
  constructor(props) {
    super(props);

    this.state = {
      id: this.props.id,
      item: '',
      dateExp: '',
      dateBought: '',
      choices: ["beef", "chicken", "pork"],
    };

    this.changeItemName = this.changeItemName.bind(this);
    this.changeDateExp = this.changeDateExp.bind(this);
    this.changeDateBought = this.changeDateBought.bind(this);
    this.update = this.update.bind(this);
    this.getItemChoies = this.getItemChoices.bind(this);

    this.update();
    this.getItemChoices();
  }

  changeItemName(event) {
    this.setState({item: event.target.value});
    this.update();
  }

  changeDateExp(event) {
    this.setState({dateExp: event.target.value});
    this.update();
  }
  
  changeDateBought(event) {
    this.setState({dateBought: event.target.value});
    this.update();
  }

  update() {
    this.props.update(this.state.id - 1, [this.state.item, this.state.dateExp, this.state.dateBought]);
  }
  

  render() {
    return(
      <div className="perishable-field">
        <div className="perishable-field-name">
          <label className="perishable-field-item">
            {'Item ' + this.state.id + ': '}
            <input
              id={'item-' + this.state.id}
              className="perishable-field-item-input"
              type="text"
              value={this.state.item}
              onChange={this.changeItemName}
              list="item-choices"
            />
            <datalist id="item-choices">
              {this.state.choices}
            </datalist>
          </label>
      </div>
        <div className="perishable-field-dates">
          <label className="perishable-field-expire">
            {"Expiration Date: "}
            <input
              id={'expire-' + this.state.id}
              className="perishable-field-expire-input"
              type="date"
              value={this.state.dateExp}
              onChange={this.changeDateExp}
            />
          </label>
          <label className="perishable-field-bought">
            {"Date Bought: "}
            <input
              id={'bought-' + this.state.id}
              className="perishable-field-bought-input"
              type="date"
              value={this.state.dateBought}
              onChange={this.changeDateBought}
            />
          </label>
        </div>
      </div>      
    );
  }

  getItemChoices() {
    fetch(this.props.backend + '/suggestions')
      .then((response) => response.json())
      .then((response) => {
          
        if (response) {
          return response;
        }
        return ["beef", "chicken", "pork"];
      }).then((choices) => {
        const comps = [];
        for (let i = 0; i < choices.length; i++) {
            comps.push(<option value={choices[i]} key={i} />);
        }
        this.setState({choices: comps});
      });
  }

}

export default PerishableField;
