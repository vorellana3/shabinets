import {Component} from "react";
import Recipe from './Recipe.js';
import './App.css';

class NewRecipe extends Component {

  constructor(props) {
    super(props);

    this.state = {
      title: "",
      ingredients: [],
      steps: [],
    };
  }

  render() {
    return (
      <Recipe title={this.state.title} ingredients={this.state.ingredients} steps={this.state.steps} />
    );
  }

  newRecipe() {
    let recipes = [
      [
        "Chocolate Chip Cookies",
        [
          "1 cup butter, softened",
          "1 cup packed brown sugar",
          "3/4 cup sugar",
          "2 large eggs, room temperature",
          "1-1/2 teaspoons vanilla extract",
          "2-2/3 cups all-purpose flour",
          "1-1/4 teaspoons baking soda",
          "1 teaspoon salt",
          "1 package (12 oz) semisweet chocolate chips",
          "2 cups coarsely choppsed walnuts, toasted"
        ],
        ["bake"]
      ],
      [
        "Peanut Butter Cookies",
        [
          "1 cup shortening",
          "1 cup peanut butter",
          "1 cup sugar",
          "1 cup packed brown sugar",
          "3 large eggs, room temperature",
          "3 cups all-purpose flour",
          "2 teaspoons baking soda",
          "1/4 teaspoon salt"
        ],
        [
          "Preheat oven to 375F",
          "In a large bowl, cream shortening, peanut butter and sugars until light and fluffy, 5-7 minutes",
          "Add eggs, 1 at a time, beating well after each addition",
          "combine flour, baking soda and salt; add to creamed mixture and mix well",
          "Roll in 1-1/2-in. balls",
          "Place 3 in. apart on ungreased baking sheets",
          "Flatten with a meat mallet or fork if desired",
          "Bake 10-15 minutes",
          "Remove to wire racks to cool"
        ],
      ],
      [
        "Lorem Ipsum pie",
        [
          "1 cup blood",
          "1 cup sweat",
          "2 cups tears",
          "a pinch of suffering",
          "screaming to taste"
        ],
        [
          "mix all the ingredients together",
          "put in microwave for 5 minutes",
          "place into the trash can to serve"
        ],
      ],
    ];
    
    let id = Math.floor(Math.random() * recipes.length);

    this.setState({
      title: recipes[id][0],
      ingredients: recipes[id][1],
      steps: recipes[id][2],
    });
  }

}

export default NewRecipe;
