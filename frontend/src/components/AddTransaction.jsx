import { useState } from "react"
import { MdClose } from "react-icons/md"

export default function AddTransaction({ setIsAdding }) {
    // Prepare state
    const [date, setDate] = useState("");
    const [amount, setAmount] = useState(0.0);
    const [memo, setMemo] = useState("");

    return (
        <>
            <div className="add-transaction-header">
                <h4>This is where a form and button will go to add a transaction</h4>
                <MdClose onClick={() => setIsAdding(false)}/>
            </div>
            <form onSubmit={ e => e.preventDefault() }>
                <p>
                    <label> Date
                        <input type="date" id="date" name="date" value={date} required
                        onChange={ e => { setDate(e.target.value) } }></input>
                    </label>
                </p>

                <p>
                    <label> Amount
                        <input type="number" id="amount" name="amount" step="0.01" value={amount}
                        onChange={ e => { setAmount(e.target.valueAsNumber) } }></input>
                    </label>
                </p>

                <p>
                    <label> Memo
                        <input type="text" id="memo" name="memo" value ={memo}
                        onChange={ e => { setMemo(e.target.value) } }></input>
                    </label>
                </p>

                <button type="submit">
                    Add
                </button>
            </form>
        </>
    )
}