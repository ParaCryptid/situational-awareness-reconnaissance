
from src.ai_engine.multimodal_fusion import MultimodalFusion

def test_multimodal_fusion():
    fusion = MultimodalFusion()
    fusion.add_text_data([0.1, 0.2, 0.3])
    fusion.add_image_data([0.4, 0.5, 0.6])
    assert fusion.fuse_data() is not None
