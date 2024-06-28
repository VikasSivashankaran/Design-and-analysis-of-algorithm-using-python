import hashlib

def read_document(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def get_hash_set(text):
    words = text.lower().split()
    hash_set = set(hashlib.sha256(word.encode()).hexdigest() for word in words)
    return hash_set

def calculate_hash_similarity(hash_set1, hash_set2):
    intersection = len(hash_set1.intersection(hash_set2))
    union = len(hash_set1.union(hash_set2))
    
    if union == 0:
        return 0.0
    
    similarity_coefficient = intersection / union
    return similarity_coefficient

def plagiarism_detection_percentage_with_hashing(document_path1, document_path2, threshold=0.5):
    text1 = read_document(document_path1)
    text2 = read_document(document_path2)
    
    hash_set1 = get_hash_set(text1)
    hash_set2 = get_hash_set(text2)
    
    similarity_coefficient = calculate_hash_similarity(hash_set1, hash_set2)
    similarity_percentage = similarity_coefficient * 100
    
    plagiarism_detected = similarity_coefficient >= threshold
    
    return plagiarism_detected, similarity_percentage

if __name__ == "__main__":
    # Example usage with document files
    document_path1 = "document1.txt"
    document_path2 = "document2.txt"
    
    plagiarism_detected, similarity_percentage = plagiarism_detection_percentage_with_hashing(document_path1, document_path2)
    
    if plagiarism_detected:
        print(f"Plagiarism detected! \nPERCENTAGE OF PLAGIARISM :{similarity_percentage:.2f}%")
    else:
        print(f"No plagiarism detected. \nPERCENTAGE OF PLAGIARISM : {similarity_percentage:.2f}%")
