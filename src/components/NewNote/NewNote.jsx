import "./NewNote.css";

const NewNote = () => {
  return (
    <div className="new-note">
      <br />
      <input type="text" className="title"></input>
      <br />
      <br />
      <textarea
        name="note-text"
        onInput="this.parentNode.dataset.replicatedValue = this.value"
        placeholder="You can always edit a bad page. You can't edit a blank page."
      ></textarea>
    </div>
  );
};

export default NewNote;
