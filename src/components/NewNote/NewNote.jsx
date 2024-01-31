import "./NewNote.css";

const NewNote = () => {
  return (
    <div className="new-note">
      <br />
      <textarea name="title" cols="16" rows="1"></textarea>
      <br />
      <br />
      <textarea name="note-text" cols="30" rows="10"></textarea>
    </div>
  );
};

export default NewNote;
