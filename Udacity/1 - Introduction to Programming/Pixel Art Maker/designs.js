/**
 * @description: creates a grid of squared
 * @param: height - number of squares that represent the height of the grid, max 25
 * @param: width - number of squares that represnt the width of the grid, max 25
 * @constructor: makeGrid
 */
function makeGrid(height, width) {
    const table = document.getElementById("pixelCanvas");
    let grid = '';

    /**
     * @param: i used to loop over each row
     * @param: j used to loop over each cell
     */
    for (let i = 0; i < height; i++) {
        grid += '<tr class="row-' + i + '">';        
        for (let j = 0; j < width; j++) {
            grid += '<td class="cell" id="row-' + i + '_cell-' + j + '"></td>';
        }
        grid += '</tr>';
    }
    
    /**
     * @constructor: to assign table.innerHTML as grid
     * @description: Used to add grid to the table
     * @description: addClickEventToCells used to add a click event after the table
     * has been created
     */
    table.innerHTML = grid;
    addClickEventToCells();
}

//Used to get the height and width from the forms to make the grid.
function formSubmission() {
    event.preventDefault();
    const height = document.getElementById('inputHeight').value;
    const width = document.getElementById('inputWidth').value;
    makeGrid(height, width);
}

//This is used to add click events to all of the cells
function addClickEventToCells() {
    //This is to return the color the user picks
    const colorPicker = document.getElementById("colorPicker");
    const cells = document.getElementsByClassName('cell');
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("click", function (event) {
            let clickedCell = event.target;
            clickedCell.style.backgroundColor = colorPicker.value;
        });
    }
}

//This is used when the user hits submit to make the grid
document.getElementById('sizePicker').onsubmit = function () {
    formSubmission();
};

//Used to make the default grid 5x5 to demonstrated grid size to user
makeGrid(5, 5);