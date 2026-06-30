import axios from "axios";

export const createShortUrl = async (originalUrl: string) => {
  const res = await axios.post("/api/shorten", {
    original_url: originalUrl,
  });
  return res.data;
};