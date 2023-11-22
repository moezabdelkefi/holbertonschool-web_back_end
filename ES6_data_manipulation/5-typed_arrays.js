export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const intArray = new Int8Array(buffer);

  if (position < 0 || position >= intArray.length) {
    throw new Error('Position outside range');
  }

  intArray[position] = value;
  return buffer;
}
