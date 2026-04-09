# Yeast Protein Localization Prediction

A deep learning project to predict subcellular localization of yeast proteins using PyTorch. The model classifies yeast proteins into 10 different cellular compartments based on their physicochemical properties.

## 📊 Dataset

- **Source**: Yeast Protein Localization Dataset (UCI Machine Learning Repository)
- **Samples**: 1,484 yeast proteins
- **Features**: 8 numerical attributes (sequence characteristics, hydrophobicity, etc.)
- **Target**: 10 subcellular localization classes
- **Train/Test Split**: 80% / 20% (stratified)

### Target Classes
| Code | Location | Description |
|------|----------|-------------|
| CYT | Cytoplasmic | Cytoplasm |
| ERL | Endoplasmic Reticulum | ER membrane |
| EXC | Extracellular | Outside cell |
| ME1 | Membrane-bound | Membrane protein type 1 |
| ME2 | Membrane-bound | Membrane protein type 2 |
| ME3 | Membrane-bound | Membrane protein type 3 |
| MIT | Mitochondrial | Mitochondria |
| NUC | Nuclear | Nucleus |
| POX | Peroxisomal | Peroxisome |
| VAC | Vacuolar | Vacuole |

## 🏗️ Model Architecture
CustomModel(
(model): Sequential(
(0): Linear(in_features=8, out_features=16, bias=True)
(1): ReLU()
(2): Linear(in_features=16, out_features=10, bias=True)
)
)

## 📈 Results

- **Training Accuracy**: 62.09%
- **Training Loss**: 0.9942
- **Training Time**: 0.25 seconds for 100 epochs

