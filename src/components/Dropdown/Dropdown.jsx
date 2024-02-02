import { useState } from "react";
// import { Link } from "react-router-dom";
import "./Dropdown.css";

const Dropdown = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown">
      <button className="dropdown-button" onClick={handleClick}>
        bobobo is {isOpen ? "open" : "closed"}
      </button>

      {/* <div className="dropdown-menu">
        {isOpen && (
          // TODO: remove the part below and replace it with the actual categories from the backend.
          <div>
            <div>
            <InputButtonComponent/>
            </div>
            <div>
            <ul>
              <li>1</li>
              <li>2</li>
              <li>3</li>
              <li>4</li>
            </ul>
            </div>
          </div>
        )}
      </div> */}
      {isOpen && (
        <div className="dropdown-add-main">

          <div className="dropdown-add-semi-main-1">
            <input type="text" placeholder="New Categories :" className="dropdown-add-input"/>
            <button className="dropdown-add-button">ADD</button>
          </div>
          <div className="dropdown-add-semi-main-2">
            <div className="dropdown-category-container"><div className="dropdown-category-hashtag">  #</div><div className="dropdown-category-name">WWWWWWWWWWWWWWW</div></div>
            <div className="dropdown-category-container"><div className="dropdown-category-hashtag">  #</div><div className="dropdown-category-name">WWWWWWWWWWWWWWW</div></div>
            <div className="dropdown-category-container"><div className="dropdown-category-hashtag">  #</div><div className="dropdown-category-name">WWWWWWWWWWWWWWW</div></div>
            <div className="dropdown-category-container"><div className="dropdown-category-hashtag">  #</div><div className="dropdown-category-name">WWWWWWWWWWWWWWW</div></div>
            <div className="dropdown-category-container"><div className="dropdown-category-hashtag">  #</div><div className="dropdown-category-name">WWWWWWWWWWWWWWW</div></div>
            <div className="dropdown-category-container"><div className="dropdown-category-hashtag">  #</div><div className="dropdown-category-name">WWWWWWWWWWWWWWW</div></div>
          </div>
        </div>)}
    </div>
  );
};

const InputButtonComponent = () => {
  const [userInput, setUserInput] = useState("");
  const [showInput, setShowInput] = useState(false);

  const handleInputChange = event => {
    setUserInput(event.target.value);
  };

  const handleButtonPress = () => {
    setShowInput(true);
  };

  return (
    <div style={{display:"flex" , flexDirection:"column" , gap:"7px"}}>
      <input
        type="text"
        value={userInput}
        
        onChange={handleInputChange}
        placeholder="Type something..."
        style={{width:"70%" , height:"25px"}}
      />
      <button onClick={handleButtonPress}>Press me</button>

      {showInput && <p>User input: {userInput}</p>}
    </div>
  );
};
export default Dropdown;
