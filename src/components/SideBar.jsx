const SideBar = () => {
  return (
    <div className="sidebar">
      <button className="upper">hi</button>
      <select className="dropdown">
        <option selected disabled>
          Select a category.
        </option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </select>
    </div>
  );
};

export default SideBar;
