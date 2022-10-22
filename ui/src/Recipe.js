import {Component} from "react";


class Recipe extends Component {
  constructor(props) {
    super(props);
    
    this.getIngredientsComp = this.getIngredientsComp.bind(this);
  }


  render() {
    return (
      <div className="recipe">
        <div className="recipe-title">{this.props.title}</div>
        {this.getIngredientsComp(this.props.ingredients)}
        {this.getSteps(this.props.steps)}
      </div>
    );
  }

  getIngredientsComp(ingredientsList) {
    const comps = [];
    for (let i = 0; i < ingredientsList.length; i++) {
      comps.push(<li className="ingredient" key={i}>{ingredientsList[i]}</li>);
    }
    return <ul className="recipe-ingredients">{comps}</ul>;
  }

  getSteps(stepsList) {
    const comps = [];
    for (let i = 0; i < stepsList.length; i++) {
      comps.push(
        <li className="step" key={i}>{stepsList[i]}</li>
      );
    }
    return <ol className="steps">{comps}</ol>;
  }

}

export default Recipe;
