// React functions
import { useState } from 'react';

export default function EditSummary({ summary, setIsEditingSummary, onSummaryEdit }) {
    // Prepare state to store new summary
    const [summaryBudget, setSummaryBudget] = useState(summary.budget);

    return (
        <form className='edit-summary-form' onSubmit={async (e) => {
                e.preventDefault();
                onSummaryEdit(summary.id, summaryBudget);
                setIsEditingSummary(false);
            }}>
            <p>
                <input type='number' id='budget-amount' name='budget-amount' value={summaryBudget} required
                onChange={e => { setSummaryBudget(e.target.valueAsNumber) }}></input>
            </p>
            <p>
                <button type='submit'>
                    Save
                </button>
            </p>
        </form>
    )
}