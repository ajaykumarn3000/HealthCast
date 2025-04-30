import React from "react";

const InputField = ({ label, type, name, placeholder, data, setData }) => {
  return (
    <div className="InputFields my-2 flex flex-col gap-2">
      <label className="font-bold text-xl " htmlFor={name}>
        {label}
      </label>
      <input
        required
        type={type}
        name={name}
        value={data}
        onChange={(e) => setData(e.target.value)}
        placeholder={placeholder}
        className={`border-[3px] px-2 py-1 border-solid rounded-lg focus:border-orange-300 ${
          data !== "" ? "border-green-500" : "border-gray-500 "
        }`}
      />
    </div>
  );
};

export default InputField;
