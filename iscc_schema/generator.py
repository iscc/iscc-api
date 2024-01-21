# generated by datamodel-codegen:
#   filename:  iscc-generator.yaml

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

try:
    from pydantic.v1 import Field
except ImportError:
    from pydantic import Field
from iscc_schema.fields import AnyUrl
from iscc_schema.base import BaseModel


class MediaUpload(BaseModel):
    """
    Media Upload
    """

    source_file: Optional[bytes] = Field(None, description="The file used for generating the ISCC.")
    source_url: Optional[AnyUrl] = Field(
        None,
        description="URL of file used for generating the ISCC.",
        example="https://picsum.photos/200/300.jpg",
    )


class MediaID(BaseModel):
    """
    Media-ID
    """

    media_id: Optional[str] = Field(
        None, description="Media file ID", example="05VJUVTH3DCP6", max_length=13, min_length=13
    )


class MediaDownload(BaseModel):
    __root__: bytes = Field(
        ..., description="Media Download", examples=["string"], title="MediaDownload"
    )


class FieldType(Enum):
    """
    The type of digital content according to schema.org classes.
    """

    AudioObject = "AudioObject"
    ImageObject = "ImageObject"
    CreativeWork = "CreativeWork"
    TextDigitalDocument = "TextDigitalDocument"
    VideoObject = "VideoObject"


class Mode(Enum):
    """
    The perceptual mode used to create the ISCC-CODE.
    """

    text = "text"
    image = "image"
    audio = "audio"
    video = "video"
    mixed = "mixed"


class IsccMetadata(BaseModel):
    """
    ISCC Metadata
    """

    field_context: Optional[AnyUrl] = Field(
        "http://purl.org/iscc/context/0.3.2.jsonld",
        alias="@context",
        description="The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.",
    )
    field_type: Optional[FieldType] = Field(
        None,
        alias="@type",
        description="The type of digital content according to schema.org classes.",
        example="ImageObject",
    )
    field_schema: Optional[AnyUrl] = Field(
        "http://purl.org/iscc/schema/0.3.2.json",
        alias="$schema",
        description="The [JSON Schema](https://json-schema.org/) URI of the ISCC metadata schema.",
    )
    iscc: Optional[str] = Field(
        None,
        description="An **ISCC-CODE** in canonical representation.",
        example="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
        max_length=73,
        min_length=15,
        regex="^ISCC:[A-Z2-7]{10,73}$",
    )
    media_id: Optional[str] = Field(
        None,
        description="Vendor specific internal identifier for media file.",
        example="05VJUVTH3DCP6",
        max_length=13,
        min_length=13,
    )
    name: Optional[str] = Field(
        None,
        description=(
            "The title or name of the intangible creation manifested by the identified *digital"
            " content*."
        ),
        example="The Secret Adversary",
        max_length=128,
    )
    description: Optional[str] = Field(
        None,
        description="Description of the *digital content* identified by the **ISCC**.",
        example="A 2001 fantasy film directed by Chris Columbus and distributed by Warner Bros.",
        max_length=4096,
    )
    meta: Optional[str] = Field(
        None,
        description="Extended metadata, wrapped in a Data-URL string.",
        example="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0=",
        max_length=16384,
    )
    creator: Optional[str] = Field(
        None,
        description="An entity primarily responsible for making the resource.",
        example="Agatha Christie",
    )
    license: Optional[AnyUrl] = Field(
        None,
        description="URL of license for the digital content.",
        example="https://example.com/license-terms-for-this-item",
    )
    acquire: Optional[AnyUrl] = Field(
        None,
        description="URL for acquiring a license for the item.",
        example="https://example.com/buy-this-item-here",
    )
    mode: Optional[Mode] = Field(
        None, description="The perceptual mode used to create the ISCC-CODE.", example="video"
    )
    mediatype: Optional[str] = Field(
        None,
        description=(
            "The [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml)"
            " (MIME type) of the referenced content."
        ),
        example="image/png",
    )
    filename: Optional[str] = Field(
        None,
        description=(
            "Filename of the referenced **digital content** (automatically used as fallback if the"
            " `name` field was not specified for ISCC processing)"
        ),
        example="some-file.png",
    )
    filesize: Optional[int] = Field(
        None, description="File size of media asset in number of bytes.", example=16896
    )
    characters: Optional[int] = Field(
        None,
        description="Number of text characters (code points after Unicode normalization)",
        example=55689,
    )
    pages: Optional[int] = Field(
        None, description="Number of pages (for paged documents only)", example=77
    )
    language: Optional[str] = Field(
        None,
        description="Main language of content [BCP 47](https://tools.ietf.org/search/bcp47).",
        example="en-US",
    )
    fps: Optional[float] = Field(None, description="Frames per second of video assets.", example=24)
    width: Optional[int] = Field(
        None, description="Width of visual media in number of pixels.", example=640
    )
    height: Optional[int] = Field(
        None, description="Height of visual media in number of pixels.", example=480
    )
    duration: Optional[int] = Field(
        None, description="Duration of audio-visual media in secondes.", example=67
    )
    generator: Optional[str] = Field(
        None, description="Name and version of the software that generated the ISCC"
    )
    created: Optional[datetime] = Field(
        None, description="Datetime the ISCC was created for the item."
    )
    metahash: Optional[str] = Field(
        None,
        description=(
            "A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the ISCC seed"
            " metadata. The hash is created from `name` and `description` fields or `meta` if"
            " supplied."
        ),
        example="f01551220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9",
        min_length=40,
    )
    datahash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default"
            " blake3)."
        ),
        example="bdyqk6e2jxh27tingubae32rw3teutg6lexe23qisw7gjve6k4qpteyq",
        min_length=40,
    )
    tophash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of"
            " metahash and datahash."
        ),
        example="bdyqnosmb56tqudeibogyygmf2b25xs7wpg4zux4zcts2v6llqmnj4ja",
        min_length=40,
    )
    thumbnail: Optional[AnyUrl] = Field(
        None,
        description=(
            "URI for a user-presentable image that serves as a preview of the digital content. The"
            " URI may be a Data-URL RFC2397."
        ),
        example="https://picsum.photos/200/300.jpg",
    )


class NftMetadata(BaseModel):
    """
    NFT Metadata
    """

    field_context: Optional[AnyUrl] = Field(
        None,
        alias="@context",
        description="The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.",
        example="http://purl.org/iscc/context",
    )
    field_type: Optional[FieldType] = Field(
        None,
        alias="@type",
        description="The type of digital content according to schema.org classes.",
        example="ImageObject",
    )
    field_schema: Optional[AnyUrl] = Field(
        None,
        alias="$schema",
        description="The [JSON Schema](https://json-schema.org/) URI of the ISCC metadata schema.",
        example="http://purl.org/iscc/schema",
    )
    iscc: Optional[str] = Field(
        None,
        description="The **ISCC-ID** of the digital content.",
        example="ISCC:MEAJU5AXCPOIOYFL",
        regex="^ISCC:[A-Z2-7]{10,73}$",
    )
    name: Optional[str] = Field(
        None,
        description=(
            "The title or name of the intangible creation manifested by the identified *digital"
            " content*."
        ),
        example="The Secret Adversary",
        max_length=128,
    )
    description: Optional[str] = Field(
        None,
        description="Description of the *digital content* identified by the **ISCC**.",
        example="A 2001 fantasy film directed by Chris Columbus and distributed by Warner Bros.",
        max_length=4096,
    )
    image: Optional[AnyUrl] = Field(
        None,
        description=(
            "URL of the actual digital content represented by the NFT or a preview of it if"
            " animation_url is provided."
        ),
        example="https://picsum.photos/200/300.jpg",
    )
    animation_url: Optional[AnyUrl] = Field(
        None, description="URL of the actual digital content (video, audio ...)"
    )
    attributes: Optional[List[Dict[str, Any]]] = Field(
        None,
        description=(
            "Attributes of the NFT artwork. These attributes will show up on NFT marketplaces."
        ),
        example=[
            {"trait_type": "METAL", "value": "SILVER"},
            {"display_type": "number", "trait_type": "GENERATION", "value": 1},
        ],
    )
    properties: Optional[Dict[str, Any]] = Field(
        None,
        description=(
            "Arbitrary properties. Values may be strings, numbers, object or arrays. Properties"
            " defined here may show up on NFT marketplaces. See"
            " [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)"
        ),
    )
    external_url: Optional[AnyUrl] = Field(
        None,
        description=(
            "This is the URL that will appear below the asset's image on some NFT Marketplaces and"
            " will allow users to leave the site and view the item on your site."
        ),
        example="https://example.com/link-to-here-from-marketplace",
    )
    license: Optional[AnyUrl] = Field(
        None, description="URI of license for the identified digital content."
    )
    original: Optional[bool] = Field(
        None,
        description=(
            "Whether the signee of the declaring transaction claims to be the original creator of"
            " the work manifested by the identified digital content."
        ),
    )
    redirect: Optional[AnyUrl] = Field(
        None,
        description=(
            "URL to which an ISCC resolver should redirect the ISCC-ID. **Supports URI template"
            " `(iscc-id)`**"
        ),
        example="https://example.com/redirect-here-for-iscc-id",
    )
    verifications: Optional[List[AnyUrl]] = Field(
        None,
        description=(
            "A list of self-verifications. Self-verifications are public URLs under the"
            " account/authority of the signee. The verification URL must respond to a GET request"
            " with text that contains a multihash of the ISCC declaration signees wallet address in"
            " the format of `verify:<multihash-of-wallet-address>:verify`."
        ),
        example=["https://twitter.com/titusz/status/1490104312051257347"],
    )


class NftPackage(BaseModel):
    """
    NFT Package
    """

    nft_id: str
    nft_metadata: Optional[NftMetadata] = None
    nft_image: Optional[AnyUrl] = None
    nft_animation: Optional[AnyUrl] = None
    iscc_code: Optional[str] = Field(
        None,
        description="An **ISCC-CODE** in canonical representation.",
        example="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
        max_length=73,
        min_length=15,
        regex="^ISCC:[A-Z2-7]{10,73}$",
    )


class IsccBasicMetadata(BaseModel):
    """
    Basic ISCC Metadata
    """

    name: Optional[str] = Field(
        None,
        description="The title or name of the creation manifested by digital content.",
        example="The Secret Adversary",
        max_length=128,
    )
    description: Optional[str] = Field(
        None,
        description="Description of the digital content.",
        example="A 2001 fantasy film directed by Chris Columbus and distributed by Warner Bros.",
        max_length=4096,
    )
    meta: Optional[str] = Field(
        None,
        description=(
            "Subject, industry, or use-case specific metadata. (Encoded as JSON string or Data-URL)"
        ),
        example="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0=",
        max_length=16384,
    )


class TaskStatus(BaseModel):
    """
    Status of an ISCC processing task
    """

    task_id: str = Field(
        ...,
        description="Unique identifier of the task.",
        example="95dcc4952deb409e81d16ab7a1338648",
    )
    started: Optional[datetime] = Field(None, example="2021-01-21T17:32:28Z")
    stopped: Optional[datetime] = Field(None, example="2021-01-21T17:34:36Z")
    success: Optional[bool] = None
    result: Optional[str] = Field(
        None, example="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
    )


class Message(BaseModel):
    """
    Informational message to the client
    """

    detail: Optional[str] = Field(
        None,
        description="Informational message about the request.",
        example="Either source_file or source_url must be provided.",
    )


class NftFrozen(BaseModel):
    """
    Frozen NFT
    """

    token_id_hex: Optional[str] = Field(
        None,
        description="NFT Token-ID (uint256 encoded as hex). ",
        example="b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9",
    )
    token_id_num: Optional[str] = Field(
        None,
        description="NFT Token-ID (uint256 digits as string)",
        example="83814198383102558219731078260892729932246618004265700685467928187377105751529",
    )
    metadata_ipfs_uri: Optional[AnyUrl] = Field(
        None,
        description="IPFS-URI of NFT metadata in base16 (hex) encoding. ",
        example="ipfs://f01551220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9",
    )
    metadata_ipfs_payload: Optional[str] = Field(
        None,
        description="JCS serialized and base64 encoded NFT metadata for publishing to IPFS",
        example="aGVsbG8gd29ybGQ=",
    )


class IsccExtraMetadata(BaseModel):
    """
    Additional embeddable metadata
    """

    creator: Optional[str] = Field(
        None,
        description="An entity primarily responsible for making the resource.",
        example="Agatha Christie",
    )
    license: Optional[AnyUrl] = Field(
        None,
        description="URL of license for the digital content.",
        example="https://example.com/license-terms-for-this-item",
    )
    acquire: Optional[AnyUrl] = Field(
        None,
        description="URL for acquiring a license for the item.",
        example="https://example.com/buy-this-item-here",
    )


class Chain(Enum):
    """
    The blockchain ISCC-CODE declaration.
    """

    BITCOIN = "BITCOIN"
    ETHEREUM = "ETHEREUM"
    POLYGON = "POLYGON"


class NftPostRequest(BaseModel):
    media_id_image: str = Field(
        ...,
        description="The `media_id` of the image for the NFT",
        example="05VJUVTH3DCP6",
        max_length=13,
        min_length=13,
    )
    media_id_animation: Optional[str] = Field(
        None,
        description="Optional `media_id` of an animation for the NFT",
        example="05VJUVTH3DCP6",
        max_length=13,
        min_length=13,
    )
    attributes: Optional[List[Dict[str, Any]]] = Field(
        None,
        description=(
            "Similar to properties but as an array of objects. These attributes will show up on"
            " some NFT marketplaces."
        ),
    )
    properties: Optional[Dict[str, Any]] = Field(
        None,
        description=(
            "Arbitrary properties. Values may be strings, numbers, object or arrays. Properties"
            " defined here may show up on NFT marketplaces. See"
            " [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)"
        ),
    )
    external_url: Optional[AnyUrl] = Field(
        None,
        description=(
            "This is the URL that will appear below the asset's image on some NFT Marketplaces and"
            " will allow users to leave the site and view the item on your site."
        ),
    )
    chain: Optional[Chain] = Field(
        None, description="The blockchain ISCC-CODE declaration.", example="POLYGON"
    )
    wallet: Optional[str] = Field(
        None,
        description="The wallet-address used for ISCC-CODE decleration.",
        example="0xb794f5ea0ba39494ce839613fffba74279579268",
    )
    original: Optional[bool] = Field(
        None,
        description=(
            "The signee of the declaring transaction claims to be the original creator of the work"
            " manifested by the identified digital content."
        ),
    )
    redirect: Optional[AnyUrl] = Field(
        None,
        description=(
            "URL to which an ISCC resolver should redirect the ISCC-ID. **Supports URI template"
            " `(iscc-id)`**"
        ),
    )
    verifications: Optional[List[AnyUrl]] = Field(
        None,
        description=(
            "A list of self-verifications. Self-verifications are public URLs under the"
            " account/authority of the signee. The verification URL must respond to a GET request"
            " with text that contains a multihash of the ISCC declaration signees wallet address in"
            " the format of `verify:<multihash-of-wallet-address>:verify`."
        ),
    )


class NftFreezePostRequest(BaseModel):
    """
    Any JSON object that can be serialized with JCS canonicaliztion.
    """


class MediaEmbeddedMetadata(IsccExtraMetadata, IsccBasicMetadata):
    """
    Media Metadata
    """


class IsccCodePostRequest(MediaEmbeddedMetadata, MediaUpload):
    pass
