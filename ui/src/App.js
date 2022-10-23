import logo from './oven-kitchen-tool-for-cooking-foods.svg';
import './App.css';
import {Component} from 'react';
import Recipe from './Recipe.js';
import PerishablePrompt from './PerishablePrompt.js';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      page: "newrecipe",
      title: "",
      ingredients: [],
      steps: "",
    };


    this.errorPage = this.errorPage.bind(this);
    this.getPage = this.getPage.bind(this);
    this.newRecipe = this.newRecipe.bind(this);
  }
  
  render() {
    return (
      <div>
        <div className="topbar">
          <div className="topbar-button topbar-recipe-recommendation" onClick={this.newRecipe}>
            New Recipe
          </div>
      <div className="topbar-button topbar-perishables-prompt" onClick={() => this.setState({page: "perishables"})}>
            Input Perishables
          </div>
        </div>
        <div className="mainbody">
          {this.getPage()}
        </div>
      </div>
    );
  }

  getPage() {
    switch(this.state.page) {
      case "newrecipe": return <Recipe title={this.state.title} ingredients={this.state.ingredients} steps={this.state.steps}/>
      case "perishables": return <PerishablePrompt header="Enter your perishables" fieldCount={0} />
      default: return this.errorPage();
    }
  }

  errorPage() {
    return (
      <div className="error-page">
        <header className="error-page-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Shabinets Error
          </p>
        </header>
      </div>
    );
  }

  newRecipe() {
    let api = "http://localhost:5000/new-recipe";
    fetch(api).then(response => response.json()).then(output => 
        this.setState({
            title: output['recipe']['label'],
            ingredients: output['recipe']['ingredientLines'],
            steps: output['recipe']['url'],
        }));
        //console.log(output));
    return;
  }
  

}

export default App;
