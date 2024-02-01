import "./NewNote.css";

const NewNote = () => {
  return (
    <div className="new-note">
      <div className="head">
        <input type="text" className="title" placeholder="Enter Title"></input>
        <div className="category">hi</div>
        <button className="save-button"> Save </button>
      </div>

      <textarea
        name="note-text"
        placeholder="You can always edit a bad page. You can't edit a blank page."
      ></textarea>
    </div>
  );
};

export default NewNote;
