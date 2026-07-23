from typing import List  # it is used for the hinting the text

from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter  #We use this splitter because it tries to split intelligently

from src.config import CHUNK_SIZE, CHUNK_OVERLAP #import chucksize or ovelap,from the file config

def split_documents(documents: List[Document]) -> List[Document]: # split the document in small chunks it means the function returns the list of ducments, by this in smaller

    splitter = RecursiveCharacterTextSplitter(  # we crete an object made from this splitter
        
        chunk_size=CHUNK_SIZE, # chunk size we did 1000 we config this

        chunk_overlap = CHUNK_OVERLAP,

        length_function=len, #for count of chunks or charecter

        is_separator_regex=False,  #regular expression use for split normal
    )

    chunks = splitter.split_documents(documents)  #  this is where everthing happen it split 9000 documents in chunks,
    # every chunk is still a langhain document

    return chunks  # give the chunked document back to whoever called the function