import { useState } from "react";

export default function Summary({ summary }) {
    // Guard against slow return of db object
    if(!summary) {
        return <div>Summary loading...</div>;
    }
    
    // Prepare state
    const [budget, setBudget] = useState(summary.budget)
    const [last_updated, setLastUpdated] = useState(summary.last_updated)

    return (
        <div className="summary">
            <div className="summary-budget">
                <h4>Budget</h4>
                <p>{budget}</p>
            </div>

            <div className="summary-spent">
                <h4>Spent</h4>
                <p>{last_updated}</p>
            </div>

            <div className="summary-remaining">
                <h4>Remaining</h4>
                <p>TODO</p>
            </div>
        </div>
    );
}