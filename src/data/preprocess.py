import torch
from  transformers import BertTokenizer
import pandas as pd

def tokenize_and_save(csv_path, split_name, tokenizer, max_len=128):

    """
    Tokenizes text data using a BERT tokenizer and saves input_ids and attention_mask as .pt files.

    Parameters:
        csv_path (str): Path to the CSV file containing the data. Must include a 'text' column.
        split_name (str): Name of the dataset split (e.g., 'train', 'val', or 'test'), used for naming output files.
        tokenizer (transformers.PreTrainedTokenizer): A Huggingface tokenizer, e.g., BertTokenizer.
        max_len (int): Maximum sequence length for padding/truncation (default is 128).

    Saves:
        - data/processed/{split_name}_input_ids.pt
        - data/processed/{split_name}_attention_mask.pt

    Author: Siqi Hsiang
    """

    df = pd.read_csv(csv_path)
    texts = df['text'].str.lower().str.strip().tolist()

    encodings = tokenizer(
        texts,
        padding='max_length',
        truncation=True,
        max_length=max_len,
        return_tensors='pt'
    )

    torch.save(encodings['input_ids'], f"data/processed/{split_name}_input_ids.pt")
    torch.save(encodings['attention_mask'], f"data/processed/{split_name}_attention_mask.pt")

if __name__ == "__main__":
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    tokenize_and_save("data/processed/train.csv", "train", tokenizer)
    tokenize_and_save("data/processed/val.csv", "val", tokenizer)
    tokenize_and_save("data/processed/test.csv", "test", tokenizer)

    print("BERT tokenization complete. Saved .pt files.")
