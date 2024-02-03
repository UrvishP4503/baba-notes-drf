import { useState } from "react";
// import { Link } from "react-router-dom";
import "./Dropdown.css";

const Dropdown = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [addNewCategory, setAddNewCategory] = useState(false);

  const handleClickOpen = () => {
    setIsOpen(!isOpen);
  };

  const handleClickNewCategory = () => {
    setAddNewCategory(!addNewCategory);
  };
  return (
    <div className="dropdown">
      <button className="dropdown-button" onClick={handleClickOpen}>
        Categories
      </button>

      {isOpen && (
        <div className="dropdown-add-main">
          <button className="dropdown-button" onClick={handleClickNewCategory}>
            {addNewCategory ? "Close" : "Add New Category"}
          </button>
          {addNewCategory && (
            <div className="dropdown-add-new-category">
              <input
                type="text"
                placeholder="New Categories :"
                className="dropdown-add-input"
              />
              <button className="dropdown-add-button">ADD</button>
            </div>
          )}

          {/* <div className="dropdown-category-container">
                <div className="dropdown-category-hashtag"> #</div>
                <div className="dropdown-category-name">WWWWWWWWWWWWWWW</div>
              </div> */}
          {!addNewCategory && (
            <div className="dropdown-add-semi-main-2">
              <div className="dropdown-category-container">
                <div className="dropdown-category-hashtag">#</div>
                <div className="dropdown-category-name">WWWWWWWWWWWWWWW</div>
              </div>
              <div className="dropdown-category-container">
                <div className="dropdown-category-hashtag">#</div>
                <div className="dropdown-category-name">WWWWWWWWWWWWWWW</div>
              </div>
              <div className="dropdown-category-container">
                <div className="dropdown-category-hashtag">#</div>
                <div className="dropdown-category-name">WWWWWWWWWWWWWWW</div>
              </div>
              <div className="dropdown-category-container">
                <div className="dropdown-category-hashtag"> #</div>
                <div className="dropdown-category-name">WWWWWWWWWWWWWWW</div>
              </div>
              <div className="dropdown-category-container">
                <div className="dropdown-category-hashtag"> #</div>
                <div className="dropdown-category-name">WWWWWWWWWWWWWWW</div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Dropdown;
