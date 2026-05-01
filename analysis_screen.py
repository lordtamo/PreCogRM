# analysis_screen.py

"""
Module dedicated to handling the creation and management of a new Risk Analysis 
within PreCogRM, compliant with EBIOS Risk Manager methodology requirements.

This screen serves as the entry point for defining the scope and context 
of an entire risk assessment before any workshop data is collected.
Data validation ensures adherence to mandatory fields and correct types 
(UUIDs, dates, enums). All persistence happens via structured JSON objects.
"""

import uuid
from datetime import date
from typing import Dict, Any, Optional

# --- Configuration and Constants ---

# Define the initial state of a new analysis based on initial_analysis.json.
DEFAULT_ANALYSIS_DRAFT: Dict[str, Any] = {
    "analysis_id": str(uuid.uuid4()), # Unique identifier for tracking
    "analysis_name": "",
    "beneficiary_name": "",
    "analysis_service": None,  # Enum lookup required
    "analyst_id": None,       # UUID lookup required
    "start_date": date.today().isoformat(), # Default to today's date
    "dsil_exists": False,     # Mandatory boolean choice, default false
    "analysis_context_type_id": None, # UUID lookup required for the framework/context
    "scope": {
        "scope_name": "",
        "scope_type": "",
        "scope_summary": "",
        "scope_description": "",
        "out_of_scope": ""
    },
    # Metadata fields, initialized from initial_analysis.json structure
    "analysis_status": "draft", # Mandatory rule: newly created analysis is 'draft'
    "analysis_version": "v1.0",
    "regulatory_frameworks": [],
    "audit_metadata": {
        "created_at": date.today().isoformat(),
        "created_by": "",
        "updated_at": None,
        "updated_by": ""
    }
}

# List of mandatory fields for UI validation (based on the specification).
MANDATORY_FIELDS: Dict[str, str] = {
    "analysis_name": "Nom de l’analyse",
    "beneficiary_name": "Nom du bénéficiaire / client",
    "analysis_service": "Service réalisant l’analyse (Enum)",
    "analyst_id": "Analyste responsable (UUID)",
    "start_date": "Date de démarrage",
    "dsil_exists": "Existence d'un DSIL", # Boolean checkbox
    "analysis_context_type_id": "Cadre de l’analyse (Context Type ID)" # UUID dropdown
}

# --- Core Logic Classes ---

class AnalysisCreationError(Exception):
    """Custom exception for validation failures during analysis creation."""
    pass


def validate_inputs(data: Dict[str, Any]) -> None:
    """
    Performs strict validation on the input data dictionary against business rules.
    Raises AnalysisCreationError if any rule is violated or a field is missing/incorrectly typed.

    Args:
        data: Dictionary containing all form inputs from the UI.
    """
    print("--- Starting Validation Process ---")
    
    # 1. Check for presence of mandatory fields
    for field_key, description in MANDATORY_FIELDS.items():
        if not data.get(field_key) and field_key != "dsil_exists":
            raise AnalysisCreationError(f"Validation failed: Le champ '{description}' est obligatoire et doit être renseigné.")

    # 2. Type validation for specific fields
    try:
        # UUID format check (must be provided from dropdowns/lookup services)
        if data.get("analyst_id") and not uuid.UUID(data["analyst_id"], version=4):
             raise AnalysisCreationError("Validation failed: L'ID de l'analyste responsable doit être un UUID valide.")
        
        # Date check (must be a valid date format)
        if data.get("start_date"):
            try:
                date.fromisoformat(data["start_date"])
            except ValueError:
                raise AnalysisCreationError("Validation failed: Le format de la date de démarrage est incorrect.")

        # Boolean check (dsil_exists must be a boolean representation)
        if "dsil_exists" in data and type(data["dsil_exists"]) is not bool:
             # Assuming the UI sends 'True' or 'False' strings, we enforce actual booleans
            raise AnalysisCreationError("Validation failed: Le champ DSIL doit être un choix binaire (vrai/faux).")

        # Context ID check
        if data.get("analysis_context_type_id"):
             uuid.UUID(data["analysis_context_type_id"], version=4) # Simple UUID structure validation

    except AnalysisCreationError as e:
        # Re-raise the specific error caught during type checking
        raise e
    except Exception as e:
        # Catch other potential errors (e.g., empty string passed as UUID)
        raise AnalysisCreationError(f"Validation failed lors de la vérification des types : {str(e)}")

    print("--- Validation successful. Data is valid for persistence. ---")


def save_analysis(input_data: Dict[str, Any], existing_metadata: Optional[Dict[str, Any]] = None) -> str:
    """
    Validates the input data and persists it in a structured format (JSON mock).

    Args:
        input_data: The raw dictionary of user inputs.
        existing_metadata: Metadata from a previously loaded record for updates.

    Returns:
        A confirmation message including the saved analysis ID.
    """
    print("\n*** Attempting to save Analysis Data ***")
    try:
        # Step 1: Validation (Mandatory step before persistence)
        validate_inputs(input_data)

        # Step 2: Prepare data for persistence and update metadata
        saved_data = DEFAULT_ANALYSIS_DRAFT.copy()
        saved_data.update(input_data) # Overwrite defaults with user input

        # Merge scope details (assuming scope is passed as a nested dict)
        if "scope" in input_data:
            saved_data["scope"].update(input_data["scope"])

        # Update metadata for successful save operation
        metadata = saved_data.get("audit_metadata", {}).copy()
        metadata["updated_at"] = date.today().isoformat()
        metadata["updated_by"] = "SystemUser" # Placeholder for the actual logged-in user

        # Step 3: Simulate persistence (e.g., writing to a database/file)
        print(f"SUCCESS: Analysis '{saved_data['analysis_name']}' saved successfully.")
        print(f"Status set to: {saved_data['analysis_status']} (Draft)")
        return f"Analyse ID {saved_data['analysis_id']} créée et sauvegardée avec succès. Statut : Draft."

    except AnalysisCreationError as e:
        # Handle business rule violations gracefully
        print(f"ERROR: Cannot save analysis due to validation failure. Details: {e}")
        return f"Échec de la sauvegarde : {e}"
    except Exception as e:
        # Handle unexpected system errors
        print(f"CRITICAL ERROR during persistence: {str(e)}")
        return "Échec critique lors de la sauvegarde de l'analyse. Veuillez contacter le support."


def render_analysis_form(data: Dict[str, Any]) -> str:
    """
    Generates a pseudo-HTML/Text representation of the UI form structure 
    for demonstration purposes, ensuring all fields are present and commented.

    Args:
        data: The currently loaded analysis data (can be draft or empty).

    Returns:
        A formatted string representing the structured form layout.
    """
    # This function simulates rendering the complex UI required by the spec.
    output = f"""
=======================================================
           FORMULAIRE DE CRÉATION D'ANALYSE DE RISQUES
=======================================================
[Statut Actuel : {data.get('analysis_status', 'Nouveau draft')}]

--- 1. Identification Générale ---
* Nom de l’analyse (Required, text): [Valeur actuelle: "{data.get('analysis_name', '')}"]
* Nom du bénéficiaire / client (Required, text): [Valeur actuelle: "{data.get('beneficiary_name', '')}"]

--- 2. Organisation et Responsabilités ---
* Service réalisant l’analyse (Required, dropdown): [Liste issue de la configuration]
  -> Sélection actuelle: {data.get('analysis_service', 'Non défini')}
* Analyste responsable (Required, dropdown): [Liste issue de la configuration]
  -> Sélection actuelle: {data.get('analyst_id', 'Non défini')}

--- 3. Cadre et Contexte de l'Analyse ---
* Date de démarrage (Required, date, Default: Today): 
  [Valeur actuelle: {data.get('start_date', '')}]
* Existence d’un DSIL (Required, checkbox): 
  ( ) Non / [X] Oui. Valeur actuelle: {str(data.get('dsil_exists', False))}.
    COMMENTAIRE BIEN-ÊTRE: Cette case à cocher est critique pour le suivi des livrables EBIOS RM.
* Cadre de l’analyse (Required, dropdown): [Liste issue du référentiel configuré]
  -> Sélection actuelle: {data.get('analysis_context_type_id', 'Non défini')}

--- 4. Scope de l'Analyse ---
(Champ détaillé pour définir le périmètre : Objectif, Exclusions)
* Nom du scope (text): [Valeur actuelle: "{data.get("scope", {}).get('scope_name', '')}"]
... // ... existing code for scope fields ...

--- 5. Métadonnées et Audit ---
(Affichage non éditable par l'utilisateur : ID unique, Date de création v1.0)
* Analyse ID: {data.get("analysis_id", "N/A")}
* Version: {data.get('analysis_version', 'v1.0')}

=======================================================
"""
    return output


# --- Simulation/Example Usage (Testing the flow) ---
if __name__ == '__main__':
    print("=" * 70)
    print("--- Démonstration de l'utilisation du module AnalysisCreation ---")
    
    # Exemple 1: Tentative de création valide (Simulating successful input capture)
    valid_input = {
        "analysis_name": "Analyse des risques sur le paiement en ligne",
        "beneficiary_name": "Banque Citadine S.A.",
        "analysis_service": "Direction Sécurité Informatique", # Enum
        "analyst_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", # Valid UUID
        "start_date": date.today().isoformat(),
        "dsil_exists": True, # Boolean
        "analysis_context_type_id": "b2a1c3d4-e5f6-7890-1234-567890abcdef", # Valid Context UUID
        "scope": {
            "scope_name": "Processus de paiement en ligne V2.0",
            "scope_type": "Transactionnel",
            "scope_summary": "Couverture des flux de paiement mobile et web.",
            "scope_description": "",
            "out_of_scope": "Analyse du système RH." # Explicit exclusion noted for traceability
        }
    }

    print("\n\n[SCÉNARIO 1: DONNÉES VALIDES ET COMPLÈTES]")
    # Save the data and get success message
    save_message = save_analysis(valid_input)
    print(f"\nRésultat de la sauvegarde : {save_message}")
    
    # Display the rendered form for user context
    form_output = render_analysis_form(valid_input)
    print(form_output)


    # Exemple 2: Tentative de création invalide (Simulating missing mandatory fields or bad data type)
    invalid_input = {
        "analysis_name": "Analyse incomplet",
        # Missing beneficiary_name, analyst_id, start_date, etc.
        "dsil_exists": "Oui", # Wrong type - should be boolean True/False
        "analysis_context_type_id": "invalid-uuid-format" # Invalid UUID format
    }

    print("\n\n" + "=" * 70)
    print("[SCÉNARIO 2: DONNÉES INVALIDES OU MANQUANTES]")
    # Save the data and catch the error
    save_message = save_analysis(invalid_input)
    print(f"\nRésultat de la sauvegarde : {save_message}")