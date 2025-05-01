import React, { useState } from "react";
import "./DatePickerComponent.css";

type Props = {
  onSelectDate: (date: string) => void;
};

/**
 * A date picker input that notifies parent 
 * components on date selection.
 */
function DatePickerComponent({ onSelectDate }: Props) {
  const [selectedDate, setSelectedDate] = useState("");

  /**
   * handles the change event of the date input
   */
  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    const date = e.target.value;
    setSelectedDate(date);
    onSelectDate(date);
  }

  return (
    <input
      type="date"
      value={selectedDate}
      onChange={handleChange}
      className="datepicker-input"
    />
  );
}

export default DatePickerComponent;
