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
        {this.getRecipe(this.props.steps)}
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

  getRecipe(link) {
    if (link === "") {
        return <div></div>
    }
    return <a href={link} target="_blank">Recipe</a>
  }

}

export default Recipe;
