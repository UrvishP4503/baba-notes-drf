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

      <div className="dropdown-menu">
        {isOpen && (
          // TODO: remove the part below and replace it with the actual categories from the backend.
          <div>
            <InputButtonComponent />
            <ul>
              <li>1</li>
              <li>2</li>
              <li>3</li>
              <li>4</li>
            </ul>
          </div>
        )}
      </div>
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
    <div>
      <input
        type="text"
        value={userInput}
        onChange={handleInputChange}
        placeholder="Type something..."
      />
      <button onClick={handleButtonPress}>Press me</button>

      {showInput && <p>User input: {userInput}</p>}
    </div>
  );
};
export default Dropdown;
