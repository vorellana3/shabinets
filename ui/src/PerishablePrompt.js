import {Component} from 'react';
import PerishableField from './PerishableField.js';

class PerishablePrompt extends Component {
  constructor(props) {
    super(props);

    this.perishableFields = [];
    this.state = {
      count: 0,
    };

    this.perishables = [];

    this.addPerishableField = this.addPerishableField.bind(this);
    this.submitPerishables = this.submitPerishables.bind(this);
    this.updatePerishable = this.updatePerishable.bind(this);
  }

  render() {
    return (
      <div className="perishable-prompt">
        <div className="perishable-prompt-header">{this.props.header}</div>
        <div className="perishable-form">
          {this.perishableFields}
        </div>
        <div className="button-container">
          <button className="perishable-button" onClick={this.addPerishableField}>Add new perishable</button>
          <button className="submit-perishables" onClick={this.submitPerishables}>Submit</button></div>
      </div>
    );
  }

  addPerishableField() {
    this.perishableFields.push(
      <PerishableField
        key={this.perishableFields.length}
        id={this.perishableFields.length + 1}
        update={this.updatePerishable}
      />
    );
    this.setState({count: this.perishableFields.length});
  }
  
  updatePerishable(id, inputs) {
    this.perishables[id] = inputs;
  }

  submitPerishables(event) {
    event.preventDefault();
    // submit perishables
    console.log(this.perishables);
  }

}

export default PerishablePrompt;
