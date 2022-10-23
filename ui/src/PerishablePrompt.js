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
    this.getButtonContainer = this.getButtonContainer.bind(this);
    this.pushNewField = this.pushNewField.bind(this);
    this.postData = this.postData.bind(this);
    
    for (let i = 0; i < this.props.fieldCount; i++) {
      this.pushNewField();
    }
  }

  render() {
    return (
      <div className="perishable-prompt">
        <div className="perishable-prompt-header">{this.props.header}</div>
        <div className="perishable-form">
          {this.perishableFields}
        </div>
        {this.getButtonContainer()}
      </div>
    );
  }

  getButtonContainer() {
    if(this.props.fieldCount === 0) {
      return (
        <div className="button-container">
          <button className="perishable-button" onClick={this.addPerishableField}>Add new perishable</button>
          <button className="submit-perishables" onClick={this.submitPerishables}>Submit</button>
        </div>
      );
    }
    return <div></div>
  }

  pushNewField() {
    this.perishableFields.push(
      <PerishableField
        key={this.perishableFields.length}
        id={this.perishableFields.length + 1}
        update={this.updatePerishable}
        backend={this.props.backend}
      />
    );
  }

  addPerishableField() {
    this.pushNewField();
    this.setState({count: this.perishableFields.length});
  }
  
  updatePerishable(id, inputs) {
    this.perishables[id] = inputs;
  }

  submitPerishables(event) {
    event.preventDefault();
    // submit perishables
    //console.log(this.perishables);
    for (let p of this.perishables) {
      console.log(p);
      let item = p[0];
      let exp = p[1];
      let bought = p[2];
      let amt = p[3];
      this.postData(`http://localhost:5000/${p[0]}/${p[1]}/${p[2]}/${p[3]}`).then(data => {});
    }
  }

  async postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'no-cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

}

export default PerishablePrompt;
