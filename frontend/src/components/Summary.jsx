import { useState } from "react";
import { parseISO, format } from "date-fns";

export default function Summary({ summary, totalSpent }) {
    // Guard against slow return of db object
    if(!summary) {
        return <div>Summary loading...</div>;
    }

    // Convert last_updated to mm/dd/yy format
    const last_updatedDateObj = parseISO(summary.last_updated)
    const formattedLastUpdatedDate = format(last_updatedDateObj, 'MM/dd/yy')
    
    // Prepare state
    const [budget, setBudget] = useState(summary.budget)
    const [last_updated, setLastUpdated] = useState(formattedLastUpdatedDate)

    return (
        <div className="summary">
            <div className="summary-budget">
                <h4>Budget</h4>
                <h5>{budget}</h5>
                <p>Updated: {last_updated}</p>
            </div>

            <div className="summary-spent">
                <h4>Spent</h4>
                <h5>${totalSpent}</h5>
            </div>

            <div className="summary-remaining">
                <h4>Remaining</h4>
                <h5>${budget - totalSpent}</h5>
            </div>
        </div>
    );
}